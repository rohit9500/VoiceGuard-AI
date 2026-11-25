class RiskCalculator:

    @staticmethod
    def calculate(fake_confidence,
                  scam_confidence):

        risk = (fake_confidence * 0.6) + (scam_confidence * 0.4)

        if risk > 80:
            level = "HIGH"

        elif risk > 50:
            level = "MEDIUM"

        else:
            level = "LOW"

        return round(risk,2), level