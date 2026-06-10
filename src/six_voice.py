import sounddevice as sd
import numpy as np
import requests
from librairy.dectectionOS import OS
import os
import glob
from librairy.travailJSON import *
from piper.voice import PiperVoice

class SixVoice:
    def __init__(self,dectos:OS):
        if dectos.osLinux() or dectos.osMac():
            home = os.path.expanduser("~")
            self.__model_dir = str(home)+"/.config/arrera-assistant/voice_model/"
            model_conf = str(home) + "/.config/arrera-assistant/voice.json"
        elif dectos.osWindows():
            home = os.path.join(os.path.expanduser("~"), "AppData", "Roaming")
            self.__model_dir = str(home) + "/arrera-assistant/voice_model/"
            model_conf = str(home) + "/arrera-assistant/voice.json"

        self.__list_model = glob.glob(self.__model_dir+"*.onnx")

        if not os.path.isfile(self.__model_dir):
            os.makedirs(os.path.dirname(self.__model_dir), exist_ok=True)

        if not os.path.isfile(model_conf):
            os.makedirs(os.path.dirname(model_conf), exist_ok=True)
            with open(model_conf, "x", encoding="utf-8") as f:
                json.dump({
                    "tom_onnx":"",
                    "tom_json":"",
                    "siwis_onnx":"",
                    "siwis_json":"",
                    "voice_selected":""
                           }, f, ensure_ascii=False, indent=2)

        self.__json_conf = jsonWork(model_conf)

        self.__voice_synthesizer = None



    def check_voice_model(self):
        if len(self.__list_model) == 0:
            if not self.__download_model("https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/tom/medium/fr_FR-tom-medium.onnx?download=true",
                                "https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/tom/medium/fr_FR-tom-medium.onnx.json?download=true",
                                  "tom"): # Tom
                return False
            if not self.__download_model("https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/siwis/medium/fr_FR-siwis-medium.onnx?download=true",
                                "https://huggingface.co/rhasspy/piper-voices/blob/main/fr/fr_FR/siwis/medium/fr_FR-siwis-medium.onnx.json?download=true",
                                  "siwis") : # Siwis
                return False

        return True

    def __download_model(self, link_onnx:str, link_json:str,voice_model:str):
        if not link_onnx and not link_json:
            return False

        if voice_model != "tom" and voice_model != "siwis":
            return False

        json_file = link_json.split('/')[-1].replace('?download=true','')
        onnx_path = link_onnx.split('/')[-1].replace('?download=true','')

        try :
            response = requests.get(link_onnx,stream=True)

            if response.status_code == 200:
                full_path = self.__model_dir + onnx_path

                with open(full_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                    self.__json_conf.setValeurJson(voice_model+"_onnx",full_path)

            response = requests.get(link_json, stream=True)

            if response.status_code == 200:
                full_path = self.__model_dir + json_file

                with open(full_path, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                    self.__json_conf.setValeurJson(voice_model + "_json", full_path)

            return True

        except Exception as e :
            print(e)
            return False

    def get_list_voice_model(self):
        return ["tom","siwis"]

    def set_voice_model(self,voice_model:str):
        if voice_model != "tom" and voice_model != "siwis":
            return False
        else :
            return self.__json_conf.setValeurJson("voice_selected",voice_model)

    def load_voice_model(self):

        self.__voice_synthesizer = None
        try :
            voice = self.__json_conf.getContentJsonFlag("voice_selected")
            if voice == "" or voice == "tom" :
                onnx_path = self.__json_conf.getContentJsonFlag("tom_onnx")
            else :
                onnx_path = self.__json_conf.getContentJsonFlag("siwis_onnx")
            
            if not onnx_path or not os.path.exists(onnx_path):
                return False
                
            self.__voice_synthesizer = PiperVoice.load(onnx_path)
            return True
        except Exception as e :
            print(e)
            return False

    def speak(self,texte:str):
        if texte != "":
            try:
                audio_bytes = b"".join(chunk.audio_int16_bytes for chunk in self.__voice_synthesizer.synthesize(texte))
                audio_data = np.frombuffer(audio_bytes, dtype=np.int16)
                frequence = self.__voice_synthesizer.config.sample_rate
                sd.play(audio_data, samplerate=frequence)
                sd.wait()
                return True
            except Exception as e :
                print(e)
                return False
        else :
            return False
