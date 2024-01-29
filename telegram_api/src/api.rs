use std::{
    io::{prelude::*},
    net::{TcpListener, TcpStream},
    thread,
};

fn handle_client(mut stream: TcpStream, tx: std::sync::mpsc::Sender<String>) {
    // read 20 bytes at a time from stream echoing back to stream

    loop {
        let mut read = [0; 1028];
        match stream.read(&mut read) {
            Ok(n) => {
                if n == 0 { 
                    // connection was closed
                    break;
                }
                println!("Received: {} bytes: {:?}", n,  std::str::from_utf8(&read[0..n]).unwrap());
                tx.send(String::from(std::str::from_utf8(&read[0..n]).unwrap())).unwrap();
                stream.write(b"200 OK").unwrap();
            }
            Err(err) => {
                
            }
        }
    }
}

pub fn api_thread(tx: std::sync::mpsc::Sender<String>) {
    println!("Hello from API Thread!");
    tx.send(String::from("API up")).unwrap();

    let listener = TcpListener::bind("0.0.0.0:7878").unwrap();

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                println!("New connection: {}", stream.peer_addr().unwrap());
                let tx1 = tx.clone();
                thread::spawn(move|| {
                    // connection succeeded
                    handle_client(stream, tx1)
                });
            }
            Err(e) => {
                println!("Error: {}", e);
                /* connection failed */
            }
        }
    }
}