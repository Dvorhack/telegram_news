pub mod api;
pub mod telegram;

use crate::api::api_thread;
use crate::telegram::telegram_thread;

use std::thread;
use std::sync::mpsc;

fn main() {
    println!("Hello, world!");

    let (tx, rx) = mpsc::channel();

    let handle = thread::spawn( || telegram_thread(rx) );    
    println!("Telegram Thread started!");

    let handle2 = thread::spawn( move || api_thread(tx.clone()) );    
    println!("API Thread started!");

    handle.join().unwrap();
    handle2.join().unwrap();
}
