module libfuncs;

import std.net.curl, std.stdio, std.process;
import std.file : mkdir;

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
    download("https://httpbin.org/get", "./clientran");
}
//TODO: play files
void PlayFiles(){
    auto pid = spawnProcess("./clientran");
}