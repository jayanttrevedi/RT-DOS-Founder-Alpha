"""
RT-DOS Intelligence Platform
Executive Report Engine
Version : 1.8.0
"""


class ReportEngine:

    def display(self, explanations):

        ranked = sorted(explanations, key=lambda x: x["score"], reverse=True)

        strong_buy = sum(1 for x in ranked if x["decision"] == "STRONG BUY")
        buy = sum(1 for x in ranked if x["decision"] == "BUY")
        watch = sum(1 for x in ranked if x["decision"] == "WATCH")
        hold = sum(1 for x in ranked if x["decision"] == "HOLD")
        avoid = sum(1 for x in ranked if x["decision"] == "AVOID")

        print()
        print("=" * 100)
        print("RT-DOS INTELLIGENCE PLATFORM")
        print("Founder Alpha Prototype")
        print("=" * 100)

        print()

        print("MARKET HEALTH")
        print("-" * 100)

        print(f"Assets Analysed : {len(ranked)}")
        print(f"Strong Buy      : {strong_buy}")
        print(f"Buy             : {buy}")
        print(f"Watch           : {watch}")
        print(f"Hold            : {hold}")
        print(f"Avoid           : {avoid}")

        print()

        print("=" * 100)
        print("TOP OPPORTUNITIES")
        print("=" * 100)

        for i, item in enumerate(ranked[:3], start=1):

            print(
                f"{i}. "
                f"{item['symbol']} "
                f"| Score {item['score']} "
                f"| {item['decision']}"
            )

        print()

        print("=" * 100)
        print("DETAILED MARKET INTELLIGENCE")
        print("=" * 100)

        for item in ranked:

            print()

            print(f"Asset        : {item['symbol']}")
            print(f"Score        : {item['score']}")
            print(f"Grade        : {item['grade']}")
            print(f"Decision     : {item['decision']}")
            print(f"Confidence   : {item['confidence']}%")
            print(f"Risk         : {item['risk']}")

            print()

            print("Reasons")

            if item["reasons"]:
                for reason in item["reasons"]:
                    print(f"  ✓ {reason}")
            else:
                print("  None")

            print()

            print("Warnings")

            if item["warnings"]:
                for warning in item["warnings"]:
                    print(f"  • {warning}")
            else:
                print("  None")

            print("-" * 100)

        print()
        print("SYSTEM STATUS : READY")
