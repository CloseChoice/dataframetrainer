describe('Register and Test Challenge', () => {
    it('Register new user and get a new challenge for her', () => {
        cy.setup()

        cy.visit('/authentication')
  
        cy.getByData('name-input').type('HermineGranger')
        cy.getByData('password-input').type('somepassword')
        cy.getByData('register-button').click()

        cy.visit('/new_challenge/RenameColumn')
        let userCode = `
        import pandas as pd
        import numpy as np

        df = pd.DataFrame([[1], [2], [3]], columns=["Value"])

        def transform(df: pd.DataFrame) -> pd.DataFrame:
            # once you found a solution, define this function
            return df.rename(columns={"Value": "NewColumn"})
        `
        cy.getByData("userCode").type(userCode)
        // todo: this does not work. Find the correct way to access this element
        cy.getByData("testButton").click()
        // check out: https://www.browserstack.com/guide/cypress-database-testing
    })
    }
)