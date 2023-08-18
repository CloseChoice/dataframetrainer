interface Summary {
    collected?: number;
    passed:  number;
    failed:  number;
    xfailed: number;
    xpassed: number;
    error:   number;
    skipped: number;
    total:   number;
    outcome?: number;
}

enum Outcome {
    Failed = "failed",
    Passed = "passed",
    Skipped = "skipped",
}

interface Result {
    nodeid:  string;
    type:    string;
    lineno?: number;
    deselected?: boolean;
}

export interface Collector {
    nodeid:  string;
    outcome: string ;
    result:  Result[];
    longrepr?: any;
}

export interface Crash {
    path:    string;
    lineno:  number;
    message: string;
}

interface Traceback {
    path: string;
    lineno: number;
    message: string;
}

export interface TestStage {
    duration:   number;
    outcome:    string;
    crash?:     Crash;
    traceback?: Traceback[];
    stdout?:    string;
    stderr?:    string;
    log?: any;
    longrepr?:  string;
}



export interface PyTest {
    nodeid:   string;
    lineno:   number;
    outcome:  string;
    keywords: string[];
    setup?:    TestStage;
    call?:    TestStage;
    teardown?: TestStage;
    metadata?: any;
}

export interface PytestResult {
    created:     number;
    duration:    number;
    exitcode:    number;
    root:        string;
    environment: any;
    summary:     Summary;
    collectors:  Collector[];
    tests:       PyTest[];
    warnings?: Warning[];
}













// export interface Environment {
//     Python:   string;
//     Platform: string;
//     Packages: Packages;
//     Plugins:  Plugins;
// }

// export interface Packages {
//     pytest: string;
//     py:     string;
//     pluggy: string;
// }

// export interface Plugins {
//     xdist:         string;
//     metadata:      string;
//     "json-report": string;
//     forked:        string;
// }








