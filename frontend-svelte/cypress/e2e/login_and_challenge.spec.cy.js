describe('Authentication Form', () => {
    it('Register new user and get a new challenge for her', () => {
        cy.setup()

        cy.visit('/authentication')
  
        cy.getByData('name-input').type('Hildegard')
        cy.getByData('password-input').type('123456789')
        cy.getByData('register-button').click()

        cy.visit('/new_challenge/RenameColumn')
        // Shows username in the navbar
        cy.getByData('new-challenge-button').click()
        // cy.get('button[id="new_challenge"]').click()
        cy.url().should('include', '/new_challenge')
        cy.url().should('not.equal', '/new_challenge/RenameColumn')
    })
    }
)