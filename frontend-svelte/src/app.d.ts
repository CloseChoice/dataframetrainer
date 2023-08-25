// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		interface Locals {
			auth: import("lucia").AuthRequest;
		}
		// interface Error {}
		// interface PageData {}
		// interface Platform {}
	}
	namespace Lucia {
		type Auth = import("$lib/server/lucia").Auth;
		type DatabaseUserAttributes = {
			// All additional Attributes have to be specified here
			name: String,
			role?: 'user' | 'admin',
		};
		type DatabaseSessionAttributes = {};
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

// THIS IS IMPORTANT!!!
export {};
