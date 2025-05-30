from minwon_tagging import Minwon_STT, Minwon_Tagging
from recommend_department import recommend_department

def main():
    # 1. 음성 파일 STT
    stt = Minwon_STT(minwon_ID="001")
    text = stt.doSTT("audio.wav", client_secret="")  # ← 실제 실행 시 .wav 파일 필요

    print("📝 STT 결과:", text)

    # 2. GPT 태그 추출
    tagger = Minwon_Tagging(minwon_ID="001")
    tagger.setString(text)
    tagger.setStringTag()

    what = tagger.getWhatTag()
    where = tagger.getWhereTag()
    how = tagger.getHowTag()

    print("태깅 결과:")
    print("what :", tagger.getWhatTag())
    print("where :", tagger.getWhereTag())
    print("how :", tagger.getHowTag())


    # 3. 부서 추천
    department = recommend_department(what, where, how)
    print("🏢 추천 부서:", department)

if __name__ == "__main__":
    main()

