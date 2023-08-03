describe('Authentication Form', () => {
    it('lets a user Register', async () => {
        cy.setup()

        cy.visit('/authentication')
  
        cy.getByData('name-input').type('Peter')
        cy.getByData('password-input').type('123456789')
        cy.getByData('register-button').click()

        // Redirects Home on Success
        // Is omitted for now because the pyodide loading takes too long
        // cy.location('pathname').should('eq', '/')

        // Shows username in the navbar
        cy.getByData('username-display').should('exist')

        // Cookie should exist
        const cookie = cy.getCookie('auth_session').should('exist')

    })

    // it('fails when a username is already taken', () => {
    //     cy.task('db:reseed')
    //     const queryText = "SELECT register_user_with_credentials('Peter', '1234')"
    //     cy.task('db:query', queryText)

    //     cy.visit('/authentication')
    //     cy.getByData('name').type('Peter')
    //     cy.getByData('password').type('123456789')
    //     cy.getByData('register-button').submit()

    //     cy.getByData("success-indicator").should('not.exist')
    // })



  })
