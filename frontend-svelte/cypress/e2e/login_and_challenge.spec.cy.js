describe('Authentication Form', () => {
    it('Register new user and get a new challenge for her', () => {
        const baseUrl = Cypress.config("baseUrl");
        cy.setup()
        cy.request('POST', `${baseUrl}/testapi/user`, {username: 'Hildegard', password: '123456789'})
        cy.visit('/')
        cy.getByData('new-challenge-button').click()
        cy.url().should('include', '/new_challenge')
    })
    }
)