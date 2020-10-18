module libfuncs;
import std.stdio;

import std.net.curl, std.stdio;
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
    Thread.sleep(dur!("seconds")( 5 ));
    writeln("you actually waited 5 seconds noob");
}
//TODO: play files
void PlayFiles(){
    writeln("files playing");
}