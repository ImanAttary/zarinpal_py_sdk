from src.zarinpal import ZarinPal
from src.utils.Config import Config

def inquire_transaction():
    try:
        config = Config(
            merchant_id= "223baac2-92a4-4f09-a8bf-0e43dc5b1144",  
            sandbox=True,  
        )
        zarinpal = ZarinPal(config)

        response = zarinpal.inquiries.inquire({
            #Enter authority:
            "authority": " "   
        })

        print("Inquiry Result:", response)
    except Exception as e:
        print("Error during inquiry:", e)
        if hasattr(e, "response"):
            print("Error Details:", e)
        else:
            print("No additional error details available.")

if __name__ == "__main__":
    inquire_transaction()