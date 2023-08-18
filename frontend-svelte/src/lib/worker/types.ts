// Only Types can be imported from the worker module. Otherwise an error "expose was called from main thread" will be thrown
export enum PyodideWorkerState{
    LOADING_CHALLENGE = 'loading challenge',
    IDLE = 'idle',
    RUNNING = 'running',
    TESTING = 'testing',
    INSTALLING = 'installing pyodidie',
    GENERATING_EXAMPLE = 'generating example'
}