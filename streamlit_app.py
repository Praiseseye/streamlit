{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2677ec57",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (1.30.0)\n",
      "Requirement already satisfied: altair<6,>=4.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (5.2.0)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (1.7.0)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (5.3.2)\n",
      "Requirement already satisfied: click<9,>=7.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: importlib-metadata<8,>=1.4 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (23.0)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (1.5.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (9.4.0)\n",
      "Requirement already satisfied: protobuf<5,>=3.20 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (4.25.0)\n",
      "Requirement already satisfied: pyarrow>=6.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (13.7.0)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (4.7.1)\n",
      "Requirement already satisfied: tzlocal<6,>=1.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (5.2)\n",
      "Requirement already satisfied: validators<1,>=0.2 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (0.22.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (3.1.41)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (0.8.1b0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: jinja2 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: zipp>=0.5 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from importlib-metadata<8,>=1.4->streamlit) (3.11.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from pandas<3,>=1.3.0->streamlit) (2022.7)\n",
      "Requirement already satisfied: six>=1.5 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2023.7.22)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in /Users/praiseayoade/anaconda3/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b534c7e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.write('hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e824330",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a9add0c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.write('hello world')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "899d0123",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
