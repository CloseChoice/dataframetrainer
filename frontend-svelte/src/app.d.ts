// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
}



interface UserProperties {
	id: number
	expires?: string // ISO-8601 datetime
	role: 'student' | 'teacher' | 'admin'
	password?: string
	firstName?: string
	lastName?: string
	email?: string
	phone?: string
  }
  
type User = UserProperties | undefined | null