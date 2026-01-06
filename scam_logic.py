# 가상의 로맨스 스캠 탐지 알고리즘

class ScamDetector:
    def __init__(self):
        # 사기 의심 키워드 데이터베이스
        self.danger_keywords = ["수익", "환전", "코인", "대리결제", "통장", "군인", "해외파견"]

    def analyze_message(self, message):
        score = 0
        for word in self.danger_keywords:
            if word in message:
                score += 20 # 키워드 발견 시 점수 합산
        
        if score >= 60:
            return "🚨 고위험: 사기가 의심되는 문구입니다!"
        elif score >= 20:
            return "⚠️ 주의: 금융 관련 대화에 주의하세요."
        else:
            return "✅ 안전: 특이사항이 없습니다."

# 예시 실행
detector = ScamDetector()
result = detector.analyze_message("수익 좋은 코인이 있는데 환전해줄 수 있어?")
print(result)
