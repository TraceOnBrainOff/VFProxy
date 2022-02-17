from src.VFProxy import VFProxy
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="VFProxy", description="A VoiceForge proxy to download voice clips without logging in.")
    parser.add_argument('-voice_name')
    parser.add_argument('-text')
    parser.add_argument('-encode', action='count', default=0)
    args=parser.parse_args()
    argv = vars(args)
    proxy = VFProxy()
    print(argv['voice_name'])
    print(argv['text'])
    print(argv['encode'])
    proxy.download_file(argv['voice_name'], argv['text'], encode=argv['encode']==1)
