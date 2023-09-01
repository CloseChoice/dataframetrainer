describe('Register and Test Challenge', () => {
    it('Register new user and get a new challenge for her', () => {
        cy.setup()

        cy.visit('/authentication')
  
        cy.getByData('name-input').type('HermineGranger')
        cy.getByData('password-input').type('somepassword')
        cy.getByData('register-button').click()
        cy.visit('/', {
        onBeforeLoad(win) {
            cy.stub(win.console, 'log').as('consoleLog')
            cy.stub(win.console, 'error').as('consoleError')
        }
        })

        cy.visit('/new_challenge/RenameColumn')
        let userCode = ["import pandas as pd",
                        "import numpy as np",
                        "",
                        'df = pd.DataFrame([[1], [2], [3]], columns=["Value"])',
                        "def transform(df: pd.DataFrame) -> pd.DataFrame:",
                        "# once you found a solution, define this function",
                        '    return df.rename(columns={"Value": "NewValue"})'];
        cy.get('.CodeMirror').as('codeMirrorElement');

        // remove old code from code editor
        cy.get('@codeMirrorElement').type("{selectall}{backspace}");
        // Type the new code content into the editor
        cy.get('@codeMirrorElement').type(userCode.join('\n'), { parseSpecialCharSequences: false } );

        // BIG TODO: once we have a logging information if the challenge was solved,
        // we can check here if the challenge was solved
        // todo: check if the button is not disabled and then click it
        cy.wait(10000); // Wait for 1 second (adjust the time as needed)
        cy.getByData("testButton").click()
        cy.wait(5000); // Wait for 1 second (adjust the time as needed)
        cy.getByData('testResultIcon').should('contain', '✅');
        // check out: https://www.browserstack.com/guide/cypress-database-testing
    })
    }
)
