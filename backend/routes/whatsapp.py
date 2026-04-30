# from fastapi import APIRouter, Form
# from fastapi.responses import Response
# from services.message_processor import process_message

# router = APIRouter()

# @router.post("/webhook")
# async def whatsapp_webhook(Body: str = Form(...)):

#     try:
#         print("📩 Incoming WhatsApp message:", Body)

#         result = process_message(Body)

#         print("✅ Process result:", result)

#         reply = f"""⚠️ Risk Bot Report

# Score: {result['score']}%
# Risk: {result['risk']}

# {result['message']}"""

#         return Response(
#             content=f"<Response><Message>{reply}</Message></Response>",
#             media_type="application/xml"
#         )

#     except Exception as e:
#         print("🔥 WEBHOOK ERROR:", str(e))

#         return Response(
#             content=f"<Response><Message>DEBUG ERROR: {str(e)}</Message></Response>",
#             media_type="application/xml"
#         )
from fastapi import APIRouter, Form
from fastapi.responses import Response
from services.message_processor import process_message

router = APIRouter()

@router.post("/webhook")
async def whatsapp_webhook(Body: str = Form(...)):

    result = process_message(Body)

    reply = f"""⚠️ Risk Bot Report

Score: {result['score']}%
Risk: {result['risk']}

{result['message']}"""

    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>"""

    return Response(content=xml, media_type="application/xml")