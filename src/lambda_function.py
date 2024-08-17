import random

def lambda_handler(event, context):
    # List of questions and corresponding answers
    kirk_conversations = [
        ["Mr. Spock, any readings on the sensors?", "Sensors show no signs of life, Captain."],
        ["Sulu, what's our position?", "Position is holding steady, sir."],
        ["Bones, what's the condition of the crew?", "The crew is in good health, Captain."],
        ["Uhura, open a channel to Starfleet.", "Channel open to Starfleet, awaiting orders."],
        ["Scotty, how much longer until we have warp drive?", "Warp drive will be ready in five minutes, Captain!"],
        ["Spock, any signs of intelligent life?", "No signs of intelligent life detected, Captain."],
        ["Chekov, scan for enemy vessels.", "Enemy vessels detected on long-range sensors."],
        ["Mr. Spock, what are the odds of surviving this?", "The odds of survival are 3,720 to 1, Captain."],
        ["Lieutenant, raise the shields!", "Shields raised, Captain. We're ready for anything."],
        ["Helm, set a course for the nearest starbase.", "Course plotted, Captain. Ready to engage."],
        ["Scanners picking up anything unusual?", "Scanners are picking up a strange energy signature."],
        ["Scotty, when can we achieve warp speed?", "Engineering reports we can give you warp speed in 30 seconds."],
        ["Captain, what's the status of the enemy ship?", "Captain, the enemy ship has cloaked."],
        ["We’re receiving a signal?", "We're receiving a distress signal from a nearby planet, Captain."],
        ["How are the shields holding?", "Shields are at full strength, Captain."],
        ["Phasers ready?", "Phasers are charged and ready, Captain."],
        ["Life support status?", "Life support is stable, Captain."],
        ["Communications systems operational?", "Long-range communications are fully operational, Captain."],
        ["Are we at the Neutral Zone?", "We've reached the neutral zone, Captain. Awaiting further orders."]
    ]

    # Select a random conversation (question-answer pair)
    question, answer = random.choice(kirk_conversations)

    # Return the conversation with CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # CORS header
            'Access-Control-Allow-Methods': 'GET',  # CORS: Allow only GET requests
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': f'{{"question": "{question}", "answer": "{answer}"}}'
    }
