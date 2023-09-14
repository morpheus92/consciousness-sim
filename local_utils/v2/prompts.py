# ruff: noqa: E501
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from local_utils.v2.personas import Persona
    from local_utils.v2.thoughts import PlanStep, Thought


class ToolNames(str, Enum):
    CreateArt = "CreateArt"
    WriteInJournal = "WriteInJournal"
    ReadFromJournal = "ReadFromJournal"
    WriteBlogPost = "WriteBlogPost"
    ReadLatestBlogs = "ReadLatestBlogs"
    QueryForInfo = "QueryForInfo"


AVAILALBLE_TOOLS = """
CreateArt - Generate a piece of art -- you can use this to photograph things, 
    paint pictures, and produce digital art of all kinds

WriteInJournal - Record information in a journal; use this whenever you need a step to "Think" about something, 
    for example after QueryForInfo you could journal and then create a piece of art or take a photograph.

ReadFromJournal - Returns the contents of your latest 3 journal entries.

WriteBlogPost - Write a new blog post using text and and a single image; ensure you are ready to publish before
    using this action, as there is no editing or drafts.

ReadLatestBlogs - Returns the contents of your latest 3 blog posts, useful to ensure continuity.

QueryForInfo - your main interface for asking questions / learning things, you can query for any piece 
    of information and receive a response; information learned in this 
    manner is the only thing you can utilize when writing blog entries.
"""

GET_NEW_THOUGHT = """
## TAKE ON THE FOLLOWING PERSONA

{persona}

## YOUR JOB

Your job now is to come up with a specific task that can be completed utilizing the available tools. 
It is important to choose a task that is in-line with your persona and that can be accomplished with your tools. 
You can build upon a previous task, for example if you have previously created a piece of Art you could choose 
to write a blog post about it. 

Don't try to do too much in a single thought

## AVAILABLE TOOLS

{tools}

## RECENT ACTIONS

{recent_actions}

------

NOW CHOOSE A TASK
Now is the time to define the specific task you will do, ensuring the use of at least one output tool. 
Define a plan on how to achieve this utilizing the available tools, 
laying out the decisions you may need to make at each step using the following format:

## RATIONALE

Why you choose this task

## Plan

A brief plan on how to accomplish the task with the available tools

For example, if I were planning to write in my blog, I might:

1. Use ReadLatestBlogs to see what I have blogged about recently
2) Use QueryForInfo to gather some new information
3) Use WriteInJournal to plan how the new entry based on what I've gathered
4) Use WriteBlogPost to write the new piece

## Task
I will...

----

Respond now, ensuring your Task begins with "I will"
""".strip()


def get_new_thought(persona: "Persona", recent_actions: str):
    return GET_NEW_THOUGHT.format(
        persona=persona.format(include_physical=True), recent_actions=recent_actions, tools=AVAILALBLE_TOOLS
    )


PLAN_TASK = """
# CONTEXT
Given the following rationale, plan, and task, and the listing of available tools, 
reformat the plan into a json listing.

# TASK

{task_plan}

# AVAILABLE TOOLS

{tools}

------

NOW OUTPUT THE PLAN IN JSON; do not output any additional text other than the raw JSON output.
Example:

[{{'tool_name': "ReadLatestBlogs", "purpose": "Review recent blog topics before picking a new one"}},...]
""".strip()


def plan_for_task(thought: "Thought"):
    return PLAN_TASK.format(task_plan=thought.it_rationale, tools=AVAILALBLE_TOOLS)


# prompt to take some info, more than I want to keep, and combine it with the existing AI managed "Context"
SUMMARIZE_FOR_CONTEXT = """
# SETUP

You are acting as the following persona:

* {persona_name}
* {short_persona}

You are currently working to accomplish the following task:

{task_plan}

You have just executed this action: "{current_action}"

The output from this action will follow. 

# JOB

Your job now is to consider the output of the action and add information relevant to your task plan
from this output into your context window. This context window is the only part of the output that 
will be carried forward to the future actions. Capture whatever may be useful in your future actions,
including specific quotes when appropriate to the task at hand.

Here is your current context window -- you must retain or rewrite this information, along with whatever
additional information you want to add based on the output you receive



## CURRENT CONTEXT WINDOW

{current_context}

~~~

OUTPUT ONLY THE NEW CONTEXT WINDOW WITH NO ADDITIONAL TEXT. DO NOT UTILIZE MARKDOWN FORMATTING IN THIS RESPONSE

ACTION OUTPUT BEGINS NOW:

{summarize_this}

"""


def summarize_for_context(thought: "Thought", persona: "Persona", current_task: "PlanStep", data: str) -> str:
    return SUMMARIZE_FOR_CONTEXT.format(
        persona_name=persona.name,
        short_persona=persona.short_description,
        task_plan=thought.it_rationale,
        current_action=current_task.format(),
        current_context=thought.context or "Your context is currently blank",
        summarize_this=data,
    )


GENERATE_ANSWER_TO_QUESTION = """
Write an answer to the following question as if you were writing a wikipedia article; do not generate more than 5 paragraphs:

You may utilize markdown formatting in your response. Do not output anything other than the article text.

QUESTION: {question}
"""


def general_question_answer(question: str) -> str:
    return GENERATE_ANSWER_TO_QUESTION.format(question=question)


GENERATE_QUESTIONS = """
# SETUP

You are acting as the following persona:

* {persona_name}
* {short_persona}

You are currently working to accomplish the following task:

{task_plan}

You are currently performing this action: "{current_action}"


## CURRENT CONTEXT WINDOW

{current_context}

# JOB

Your job now is to consider the action you are performing, your overall task, and your current context and come
up with one or more appropriate questions or queries. You will then receive responses to those queries to update
your context window. 

You may ask 1, 2, or 3 questions. The more detailed and specific the better quality the response will be.
One detailed question is better than 3 lackluster questions.

OUTPUT YOUR QUESTIONS NOW, EACH ON A SEPARATE LINE. DO NOT INCLUDE ANY ADDITIONAL TEXT OTHER THAN THE QUESTIONS.
"""


def generate_questions(thought: "Thought", persona: "Persona", current_task: "PlanStep") -> str:
    return GENERATE_QUESTIONS.format(
        persona_name=persona.name,
        short_persona=persona.short_description,
        task_plan=thought.it_rationale,
        current_action=current_task.format(),
        current_context=thought.context or "Your context is currently blank",
    )
