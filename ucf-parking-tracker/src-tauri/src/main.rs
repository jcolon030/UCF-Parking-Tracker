// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::{env, process::Command, thread, time::Duration};

fn main() {
     tauri::Builder::default()
        .setup(|_app| {
            // Run once at launch
            run_scraper();

            // Start background thread to scrape every 30 mins
            thread::spawn(|| {
                loop {
                    thread::sleep(Duration::from_secs(1800)); // 30 minutes
                    run_scraper();
                }
            });

            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}

fn run_scraper() {
     // Get the working directory where the app was launched from
    let project_root = env::current_dir().expect("Failed to get current directory");

    // Build path to scrape.py under src-tauri/endpoint/
    let script_path = project_root.join("endpoint").join("scrape.py");

    println!("Running scraper at: {}", script_path.display());

    let _ = Command::new("python")
        .arg(script_path)
        .spawn()
        .expect("Failed to run scraper");
}

