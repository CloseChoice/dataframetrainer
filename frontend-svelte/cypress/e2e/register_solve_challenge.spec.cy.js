describe('Register and Test Challenge', () => {
    it('Register new user and get a new challenge for her', () => {
        cy.setup()
        cy.request('POST', 'http://localhost:5173/testapi/user', {username: 'Hildegard', password: '123456789'})
        cy.visit('/authentication')
        // cy.visit('/', {
        // onBeforeLoad(win) {
        //     cy.stub(win.console, 'log').as('consoleLog')
        //     cy.stub(win.console, 'error').as('consoleError')
        // }
        // })

        cy.visit('/new_challenge/RenameColumn')
        let userCode = ["import pandas as pd",
                        "import numpy as np",
                        "",
                        'df = pd.DataFrame([[1], [2], [3]], columns=["Value"])',
                        "def transform(df: pd.DataFrame) -> pd.DataFrame:",
                        "# once you found a solution, define this function",
                        '  df_return = df.rename(columns={"Value": "NewValue"})',
                        '  return df_return'];
                        // '    return df.rename(columns={"Value": "NewValue"})'];
        // data-test="CodeMirrorClass"
        cy.get('.CodeMirror').as('codeMirrorElement');
        const cm = cy.getByData('code-mirror-root')
        cm.type("{selectall}{backspace}")
        // Type the new code content into the editor
        cm.type(userCode.join('\n'), { parseSpecialCharSequences: false } );
        cy.getByData('pyodide-state', {timeout: 20000}).should('have.attr', 'data-state', 'idle')
        const testBtn = cy.getByData("test-button")
        testBtn.should('not.be.disabled')
        testBtn.click()

        cy.getByData('test-result', {timeout: 20000}).should('have.attr', 'data-exit-code', '0')
        // cy.wait(10000); // Wait for 1 second (adjust the time as needed)
        // cy.getByData('testResultIcon').should('contain', '✅');
        // check out: https://www.browserstack.com/guide/cypress-database-testing
    })
    }
)
