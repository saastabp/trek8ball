import random

def lambda_handler(event, context):
    # Star Trek themed responses (fortunes)
    fortunes = [
        "Sensors show no signs of life, Captain.",
        "Position is holding steady, sir.",
        "The crew is in good health, Captain.",
        "Channel open to Starfleet, awaiting orders.",
        "Warp drive will be ready in five minutes, Captain!",
        "No signs of intelligent life detected, Captain.",
        "Enemy vessels detected on long-range sensors.",
        "The odds of survival are 3,720 to 1, Captain.",
        "Shields raised, Captain. We're ready for anything.",
        "Course plotted, Captain. Ready to engage.",
        "All systems are functioning within normal parameters, Captain.",
        "Scanners are picking up a strange energy signature.",
        "Engineering reports we can give you warp speed in 30 seconds.",
        "Captain, the enemy ship has cloaked.",
        "We're receiving a distress signal from a nearby planet, Captain.",
        "Shields are at full strength, Captain.",
        "Phasers are charged and ready, Captain.",
        "Life support is stable, Captain.",
        "Long-range communications are fully operational, Captain.",
        "We've reached the neutral zone, Captain. Awaiting further orders."
    ]

    # Kirk-inspired bridge questions
    kirk_questions = [
        "Mr. Spock, any readings on the sensors?",
        "Sulu, what's our position?",
        "Bones, what's the condition of the crew?",
        "Uhura, open a channel to Starfleet.",
        "Scotty, how much longer until we have warp drive?",
        "Spock, any signs of intelligent life?",
        "Chekov, scan for enemy vessels.",
        "Mr. Spock, what are the odds of surviving this?",
        "Lieutenant, raise the shields!",
        "Helm, set a course for the nearest starbase."
    ]

    # Get query parameters (if any)
    message_type = event.get('queryStringParameters', {}).get('messageType', 'fortune')

    # Choose between fortune or Kirk question
    if message_type == 'question':
        response = random.choice(kirk_questions)
    else:
        response = random.choice(fortunes)

    # Return the response with CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # CORS header
            'Access-Control-Allow-Methods': 'GET',  # CORS: Allow only GET requests
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': f'{{"message": "{response}"}}'
    }
