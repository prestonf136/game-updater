module libfuncs;

import std.net.curl, std.stdio, std.process;

import core.thread;
bool CheckVers(string currentves) {
    auto content = get("dlang.org");
    
    if ("v0.0.0" == currentves) {
        return true;
    } else {
        return false;
    }
}

//TODO:downloads
void DownloadFiles() {
    download("https://httpbin.org/get", "/tmp/downloaded");
}
//TODO: play files
void PlayFiles(){
    writeln("files playing");
    auto pid = spawnProcess("/tmp/client");
}