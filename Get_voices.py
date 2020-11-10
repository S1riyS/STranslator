""" Получаем все возможные голоса, установленные в системе """

from winreg import * # Модуль для работы с реестром


class Voices:
    @staticmethod
    def get_voices():
        m = OpenKey(HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Speech\Voices\Tokens")
        VOICES = {}

        try:
            count = 0
            while 1:
                voice = EnumKey(m, count)
                current_lang = voice.split("_")[2]
                lang = current_lang.split("-")[0].lower()
                if lang not in VOICES:
                    VOICES[lang] = (
                        r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens"
                        + f"\\{voice}"
                    )
                count += 1

        except WindowsError as err:
            return VOICES
            pass
