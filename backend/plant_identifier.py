import os
from dotenv import load_dotenv
from emergentintegrations.llm.chat import LlmChat, UserMessage, ImageContent
import json

load_dotenv()

EMERGENT_LLM_KEY = os.getenv("EMERGENT_LLM_KEY", "")

async def identify_plant_from_image(image_base64: str) -> dict:
    """
    Identify a plant from base64 image using OpenAI Vision API
    """
    try:
        # Create a new LlmChat instance for this identification
        chat = LlmChat(
            api_key=EMERGENT_LLM_KEY,
            session_id=f"plant_identification",
            system_message="You are an expert botanist specializing in Ayurvedic plants. When shown a plant image, identify it and provide detailed information including: plant name, scientific name, family, characteristics, medicinal properties, and uses. Always respond in JSON format."
        ).with_model("openai", "gpt-4o")

        # Create image content from base64
        image_content = ImageContent(image_base64=image_base64)

        # Create user message with image
        user_message = UserMessage(
            text="""Please identify this plant and provide information in the following JSON format:
{
  "plant_name": "common name of the plant",
  "scientific_name": "scientific name",
  "family": "plant family",
  "confidence": "high/medium/low",
  "characteristics": ["list of visible characteristics"],
  "medicinal_properties": ["list of medicinal properties if it's an Ayurvedic plant"],
  "uses": ["traditional uses"],
  "parts_used": ["parts typically used"],
  "description": "detailed description"
}

If you cannot identify the plant with certainty, set confidence to 'low' and provide your best guess.""",
            file_contents=[image_content]
        )

        # Get response
        response = await chat.send_message(user_message)
        
        # Parse JSON response
        try:
            # Try to extract JSON from response
            response_text = response.strip()
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            plant_data = json.loads(response_text)
            return {
                "success": True,
                "data": plant_data,
                "raw_response": response
            }
        except json.JSONDecodeError:
            # If JSON parsing fails, return raw response
            return {
                "success": True,
                "data": {
                    "plant_name": "Unknown",
                    "scientific_name": "N/A",
                    "family": "N/A",
                    "confidence": "low",
                    "characteristics": [],
                    "medicinal_properties": [],
                    "uses": [],
                    "parts_used": [],
                    "description": response
                },
                "raw_response": response
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }