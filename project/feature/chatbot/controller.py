from .data_access.factory import FactoryDataAccess
from .response_serializer.factory import FactoryResponseSerializer
from .chatbot_service.factory import FactoryChatBotService
from .excpetions import WrongQuestion
from flask import jsonify

class ChatBotController:
    def __init__(self):
        self.data_access = FactoryDataAccess.build_object()
        self.chatbot_service = FactoryChatBotService.build_object(self.data_access)
        self.response_serializer = FactoryResponseSerializer.build_object()

    def create_qa(self, validate_data):
        try:
            # Validate data
            print("Validating data:", validate_data)
            print("Calling chatbot_service.chatbot with question:", validate_data.question)
            
            # Generate an answer first using the chatbot method
            answer = self.chatbot_service.chatbot(validate_data.question)
            
            # Create QA entry
            qa = self.chatbot_service.Create_Qa(validate_data.question, answer)
            self.data_access.commit()
            
            return self.response_serializer.Serialize_ChatBot(qa)
        except (WrongQuestion, Exception) as e:
            return jsonify({"error": str(e)})

    def generate_answer(self, question):
        response = self.chatbot_service.chatbot(question)
        return jsonify({"answer": response})
