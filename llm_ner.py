from __future__ import annotations
from typing import Any, Dict, List, Text, Optional

from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message
from rasa.nlu.extractors.extractor import EntityExtractorMixin
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.shared.nlu.constants import (
  ENTITIES,
  ENTITY_ATTRIBUTE_START,
  ENTITY_ATTRIBUTE_END,
  ENTITY_ATTRIBUTE_VALUE,
  TEXT,
  ENTITY_ATTRIBUTE_TYPE
)

from langchain_core.prompts import PromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.prompt_template import format_document
from langchain_google_genai import ChatGoogleGenerativeAI
import json
import re
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyD7BIGwysJ8IykmmQYGomM8-ua27MUtXLw"

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                 temperature=0.7, top_p=0.85)

@DefaultV1Recipe.register(
  DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR, is_trainable=True
)
class CustomEntityExtractor(GraphComponent, EntityExtractorMixin):
    """Custom Entity Extractor using some custom logic."""

    @staticmethod
    def get_default_config() -> Dict[Text, Any]:
        return {
            "some_custom_config": "default_value"
        }

    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
    ) -> CustomEntityExtractor:
        return cls(config, model_storage, resource)

    def __init__(
        self,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        some_custom_config: Optional[List[Dict[Text, Text]]] = None,
    ) -> None:
        self._config = {**self.get_default_config(), **config}
        self._model_storage = model_storage
        self._resource = resource

    def train(self, training_data: TrainingData) -> Resource:
        # Implement your training logic here
        self.persist()
        return self._resource

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            entities = self._extract_entities(message)
            entities = self.add_extractor_name(entities)
            message.set(
                "entities",
                message.get("entities", []) + entities,
                add_to_output=True,
            )
        return messages

    def _extract_entities(self, message: Message) -> List[Dict[Text, Any]]:
        text = message.get("text")
        entities = []
        result = llm.invoke(f'''
          Input text: {text}
          Answer: Analyse the input text and do NER extraction for start date and end date in a json with key values as datefrom and dateto.
          ''')
        
        # print(result.content)
        
        match = re.search(r'\{.*\}', result.content, re.DOTALL)
        json_content = match.group(0)
        
        result_dict = json.loads(json_content)
        # print(result_dict['datefrom'])
        # print(result_dict['dateto'])
        
        for key, value in result_dict.items():
          start = text.find(value)
          if start != -1:
              end = start + len(value)
              entities.append({
                  "entity": key,
                  "value": value,
                  "start": start,
                  "end": end,
              })
        return entities

    def persist(self) -> None:
        # Implement the persistence logic if necessary
        pass

    @classmethod
    def load(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext,
        **kwargs: Any,
    ) -> CustomEntityExtractor:
        # Implement the load logic if necessary
        return cls(config, model_storage, resource)



