curl --location 'https://api.metisai.ir/api/v1/wrapper/openai_chat_completion/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: {METIS_API_KEY}' \
--data '{
    "model": "gpt-3.5-turbo-0125",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Who won the world series in 2020?"
      },
      {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020."
      },
      {
        "role": "user",
        "content": "Where was it played?"
      }
    ]
  }'