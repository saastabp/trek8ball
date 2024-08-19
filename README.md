# Star Trek Magic 8 Ball (AI)

This is a simple project to play with some of the code generation capabilities
of ChatGPT.  The goal is to create an online version of the classic Magic 8 Ball
game, but with a twist -- I wanted it to have a Star Trek theme.

Additionally, I wanted to be as 'hands-off' as possible when dealing with the
code generation, including using prompts to get ChatGPT to fix any issues I
might see in the results.

Here's how it went:

# Getting Started

The first order of business was deciding on the scope.  I was looking for:
- A serverless implementation
- Package and deploy using AWS SAM
- A basic REST API using AWS API Gateway (via SAM)
- A Star Trek theme to the Magic 8 Ball responses

I figured I would start with something simple, just asking for the lambda function.
Once that was up I would move on to creating the SAM template.  My first prompt was:

> create a lambda function that is a magic 8 ball.  The fortunes should have a star trek theme

I got back a Python lambda function with about 15 possible responses.  Calling the function
picked one at random and returned it in the body with a 200 response code.  It also provided
some basic instructions on how to run and test the function.

# Configuring SAM

After creating the lambda function, it concluded with this:

> Let me know if you'd like help with setting up the SAM template to deploy this function!

Cool!  That's what I was going to do next anyway, but there were some specifics I wanted included
in the response, so I asked for this:

> Yes, create a SAM template to add a web service as a front end.  Use a lambda proxy so that CORS is properly handled.  Update the lambda response if necessary

I got back what looked like a reasonable `template.yaml` file, and it also gave me the update version of the lambda
function to handle CORS:

```
    # Return the response with CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',  # CORS header
        },
        'body': f'{{"fortune": "{response}"}}'
    }
```

Ok, that looked good, but I noticed this in the gateway handler section of the SAM template:

'''
    Cors:
        AllowMethods: "'GET'"
        AllowHeaders: "'Content-Type'"
        AllowOrigin: "'*'"
'''

I did not expect that as I specifically asked for a proxy integration.  The gateway should not
implement CORS processing in that case, delegating that responsibility to the service.  Could
ChatGPT make the correction?  I wanted to see what it would do if I asked about what it did instead
of simply telling it to remove CORS processing from the gateway, so I said this:

> This is supposed to be a lambda proxy integration.  why is there a cors section?

It did give back a properly updated SAM template along with a description of the changes, but I found
its introductory paragraph interesting, more conversational than I expected:

> You're right to question the presence of the Cors section. For a Lambda proxy integration, the Lambda 
function is responsible for returning the appropriate CORS headers, so we do not need to specify CORS 
in the SAM template itself.

Curious that it understood what to do when I questioned it about CORS, but didn't get it right
initially, particularly when it knew enough to deal with it in the lambda.

Anyway, at this point it looked like I had enough to package and deploy the API and lambda function.
I created an S3 bucket for SAM/CloudFormation to use, then packaged and deployed the service.  I was
pleased to see that it worked right out of the gate.

# The User Interface

The next challenge was the web page.  I knew that it could create a simple Magic 8 Ball - I'd seen this
done before - but I wanted to give it a more difficult test:

> Now create an index.html page that will print the fortunes on the main view screen of the enterprise bridge.  Include the helm and navigation stations in the image.  Get the fortunes from this URL: &lt;api URL from the GET method in the API Gateway&gt;

Well ...

The web page had a button to get the fortune, and properly invoked the API, so it succeeded functionally,
but it failed miserably at finding an image of the view screen and using that to display the response.  At
this point, some manual intervention was required to find an image I liked and to adjust the position of
the text accordingly.  All in all, though, the javascript and css it produced worked well, and even had
some basic error handling.  I could live with that.

Finally, I thought it would be cool to have more of a command/response feel to the function:

> Update the lambda function to return either one of the random fortunes that it does now, or a random question that Kirk would ask of someone on the bridge.  Use a query parameter to determine which message is returned.  Leave all functional aspects of the function the same.


Accordingly, I got an updated lambda function with two lists - `fortunes` and `kirk_questions`, and a section in
the lambda like this:

```
    # Get query parameters (if any)
    message_type = event.get('queryStringParameters', {}).get('messageType', 'fortune')

    # Choose between fortune or Kirk question
    if message_type == 'question':
        response = random.choice(kirk_questions)
    else:
        response = random.choice(fortunes)
```


I also wanted the fortunes to be more in line with a response to Kirk:

> provide a list of random answers to kirk's questions as the fortunes.

Of course, it gave me exactly what I asked for - a simple list of responses in plain text.  So ...

> Use these responses in the lambda function

Lambda function updated.  Better.

With a couple of minor updates to the `index.html` file and it was working.  A command and response appeared, and
clicking the command would give a different command/response pair.  The problem is that the response was
frequently a complete non-sequitor, and I wanted the thing to make some sort of sense.

So I prompted:

> organize the questions and responses into a list of lists so that they make sense.  Remove the query parameter and return the question and corresponding answer in the same response json.
 
What I got back was a 2D list of what it called `kirk_conversations` and just picked one randomly to return.  Not
quite what I asked for, but at least it made sense.

# Summary

The purpose of this exercise was to get a feel for properly creating prompts for a GenAI
service and learning how to get to do what you want it to do.  I'm reminded of the
phrase, "Be careful what you ask for -- you might get it!"

Here is the result: [Magic 8 Ball, Star Trek Style](https://saastabp.github.io/trek8ball/)