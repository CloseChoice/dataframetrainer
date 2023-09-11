describe('Register and Test Challenge', () => {
    it('Register new user and get a new challenge for her', () => {
        const baseUrl = Cypress.config("baseUrl");
        cy.setup()
        cy.request('POST', `${baseUrl}/testapi/user`, {username: 'Hildegard', password: '123456789'})
        cy.visit('/authentication')

        cy.visit('/new_challenge/RenameColumn')
        let userCode = ["import pandas as pd",
                        "import numpy as np",
                        "",
                        'df = pd.DataFrame([[1], [2], [3]], columns=["Value"])',
                        "def transform(df: pd.DataFrame) -> pd.DataFrame:",
                        "# once you found a solution, define this function",
                        '  df_return = df.rename(columns={"Value": "NewValue"})',
                        '  return df_return'];

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
        // check out: https://www.browserstack.com/guide/cypress-database-testing
    })
    }
)
