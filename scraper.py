import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto("https://trello.com/b/QvHVksDa/personal-work-goals")

    tasks = await page.querySelectorAll('.js-card-name')

    for taskshandle in tasks:
        task = await page.evaluate('(el) => el.textContent', taskshandle)
        print(task.strip())  # Strip to remove leading/trailing white spaces

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


# Console Output 
#21Cook new recipes on the weekend
#5Research freelance possibilites
#6Land first freelance job
#22Compile list of favorite photos for photo book gift at Christmas
#9Complete software update 4.1 before September
#10Add additional functionality to database loading applications
#11Ask to be assigned to a major project
#12Complete courses required for the focus of my degree
#8Complete University Degree by 2021
#13One date night a month.
#7Continue to host "movie night" on Sunday's with friends
#1Write two posts per week.
#2Write article about Trello and how to setup life goals board
#3Get life goals board shared on the new Trello Inspiration page
#4Join bloglovin'
#15Lower blood pressure
#17Use MyFitnessPal without skipping days
#18Obtain 10,000 steps a day on average using my Fitbit
#14Run a 10k before the end of the year
#16Meditate three times a week
#19Places to See With the Kids
#20Places to See Later in Life
#23Put aside $__ per month to save for travel
#24Put aside $__ per month for investments
#25Put aside $__ per month for savings