import logging

import definition_pb2
from adapters.orm import SessionLocal
from domain.models import User


class UsersDefinition:
    def create_user(self, request, context):
        logging.info(f"Executing create_user to create {request.email} user")
        with SessionLocal() as session:
            new_user = User(
                email=request.email, hashed_password=request.hashed_password
            )

            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            session.close()

            response = definition_pb2.UserData(id=new_user.id, email=new_user.email)
            return response
