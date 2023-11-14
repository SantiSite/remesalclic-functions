# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

import logging

from firebase_functions.firestore_fn import Event, DocumentSnapshot, on_document_created
from firebase_admin import initialize_app, messaging, firestore

logging.basicConfig(level=logging.INFO)

initialize_app()


@on_document_created(document="chats/{chat_id}")
def send_push_notification_for_deal_creation(event: Event[DocumentSnapshot | None]) -> None:
    logging.info("Sending push notification for deal creation")

    # chat_id es lo mismo que el id del trato en el servidor de remesalclic
    deal_id = event.params["chat_id"]

    seller = event.data.get("seller")
    seller_token = seller['firebaseToken']
    if seller_token is None:
        logging.info("Seller has no firebase token")
        return

    buyer = event.data.get("buyer")

    message = messaging.Message(
        data={
            "deal_id": deal_id,
        },
        token=seller['firebaseToken'],
        notification=messaging.Notification(
            title="¡Tienes un nuevo trato!",
            body=f"{buyer['name']} inició un nuevo trato.\n¡Revisa tu lista de tratos para ver los detalles!"
        )
    )

    messaging.send(message)


@on_document_created(document="chats/{chat_id}/messages/{message_id}")
def send_push_notification_for_message(event: Event[DocumentSnapshot | None]) -> None:
    logging.info("Sending push notification for message")

    data = event.data.to_dict()

    # chat_id es lo mismo que el id del trato en el servidor de remesalclic
    deal_id = event.params["chat_id"]
    message_id = event.params["message_id"]

    user_type = data["user"]["userType"]

    deal = firestore.client().collection("chats").document(deal_id).get().to_dict()

    if deal is None:
        logging.info("Deal not found")
        return

    if user_type == "SELLER":
        buyer = deal["buyer"]
        token = buyer['firebaseToken']
        if token is None:
            logging.info("Buyer has no firebase token")
            return
        name = buyer['name']
    else:
        seller = deal["seller"]
        token = seller['firebaseToken']
        if token is None:
            logging.info("Seller has no firebase token")
            return
        name = seller['name']

    message = messaging.Message(
        data={
            "deal_id": deal_id,
            "message_id": message_id
        },
        token=token,
        notification=messaging.Notification(
            title="¡Tienes un nuevo mensaje!",
            body=f"{name} te envió un mensaje.\n¡Revisa tu lista de tratos para ver los detalles!"
        )
    )

    messaging.send(message)

