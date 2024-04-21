import sys
import os
import re
from pathlib import Path
from datetime import datetime

# LangChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage
)