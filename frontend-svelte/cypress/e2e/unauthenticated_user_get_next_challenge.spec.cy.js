describe('Unauthenticated user flow', () => {
    it('Go to browse_challenges and then click on a challenge get the next challenge from there', () => {
        cy.setup()

        cy.visit('/new_challenge/RenameColumn')
        // Check that url changes if we click on a challenge
        // see https://stackoverflow.com/a/56790640 for more information
        cy.url().then( url => {
          cy.get('button[id="new_challenge"]').click();
          cy.url().should('not.eq', url);
        })
    })
    }
)