import traceback
import pyrogram as pbot
from LaylaRobot.modules.gituser import *

__HELP__ = """See inline for help related to inline"""

@pbot.on_git()
async def git(client, query):
    try:
        text = query.query.strip().lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func(__HELP__)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=10
            )
            return

        elif text.split()[0] == "gh_user":
            if len(text.split()) < 2:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Github User | gh_user [USERNAME/LINK]",
                    switch_pm_parameter="inline",
                )
            tex = text.split(None, 1)[1].strip()
            answerss = await github_user_func(answers, tex)
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=2
            )

    except Exception as e:
        e = traceback.format_exc()
        print(e, " InLine")
