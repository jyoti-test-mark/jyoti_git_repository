const {test,expect} = require("@playwright/test");

test("Login to swag lab", async function({page}){

    await page.goto("https://www.saucedemo.com/");
    await page.getByPlaceholder("Username").type("standard_users");
    await page.getByPlaceholder("Password").type("secret_sauce");
    await page.getByRole('button',{name:'Login'}).click();
    await expect(page.getByText('Epic sadface: Username and password do not match any user in this service')).toBeVisible();
    //await page.locator("//button[@class='error-button']").click();
}
)