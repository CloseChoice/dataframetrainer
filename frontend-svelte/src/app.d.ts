// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		interface Locals {
			auth: import("lucia").AuthRequest;
			// Lucia doesn't provide a type for the session so this is hard coded for now
			session: {
				activePeriodExpiresAt: Date;
				fresh: Boolean;
				idlePeriodExpiresAt: Date;
				sessionId: string;
				state: string;
				user: {
					name: string;
					role: string;
					userId: string;
				}
			}
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

declare module '$env/static/private' {
    export const PUBLIC_KEY: string;
	export const NODE_ENV: string;
	export const PASSWORD: string;
	export const DB_USER: string;
	export const DB_PORT: string;
	export const DB_NAME: string;
	export const AUTH_SECRET: string;
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
