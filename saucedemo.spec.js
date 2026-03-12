const {test,expect} = require("@playwright/test")

test("Login to swag lab", async function({page}){

    await page.goto("https://www.saucedemo.com/")
    await page.getByPlaceholder("Username").type("standard_user")
    await page.getByPlaceholder("password").type("secret_sauce")
    await page.locator('input[type="submit"]').click()
    //await page.getByRole('button',{name:'Login'}).click()
    await expect(page).toHaveURL("https://www.saucedemo.com/inventory.html");
    await page.getByRole('button',{name:'Open Menu'}).click()
    //await page.getByRole('link', { name: 'Logout' }).click()
    await page.getByText("Logout").click()
}
)