describe('Authentication Form', () => {
    it('lets a user Register', () => {
        cy.task('db:reseed')

        cy.visit('/authentication')
  
        cy.getByData('name').type('Peter')
        cy.getByData('password').type('123456789')
        cy.getByData('register-button').submit()

        cy.getByData("success-indicator").should("exist")
        // The session should be set now
  
    })

    it('fails when a username is already taken', () => {
        cy.task('db:reseed')
        const queryText = "SELECT register_user_with_credentials('Peter', '1234')"
        cy.task('db:query', {queryText})

        cy.visit('/authentication')
        cy.getByData('name').type('Peter')
        cy.getByData('password').type('123456789')
        cy.getByData('register-button').submit()

        cy.getByData("success-indicator").should('not.exist')
    })



  })
