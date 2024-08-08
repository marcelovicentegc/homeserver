use tauri::{LogicalPosition, LogicalSize, WebviewUrl};

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let width = 800.;
            let height = 600.;
            let window = tauri::window::WindowBuilder::new(app, "sys-o11y")
            .inner_size(width, height)
            .build()?;
    
            let _grafana = window.add_child(
            tauri::webview::WebviewBuilder::new(
                "grafana",
                WebviewUrl::External("http://localhost:32911".parse().unwrap()),
            )
            .auto_resize(),
            LogicalPosition::new(width / 2., 0.),
            LogicalSize::new(width / 2., height / 2.),
            )?;
            let _prometheus = window.add_child(
            tauri::webview::WebviewBuilder::new(
                "prometheus",
                WebviewUrl::External("http://localhost:52441".parse().unwrap()),
            )
            .auto_resize(),
            LogicalPosition::new(0., height / 2.),
            LogicalSize::new(width / 2., height / 2.),
            )?;
            let _portainer = window.add_child(
            tauri::webview::WebviewBuilder::new(
                "portainer",
                WebviewUrl::External("http://localhost:37017".parse().unwrap()),
            )
            .auto_resize(),
            LogicalPosition::new(width / 2., height / 2.),
            LogicalSize::new(width / 2., height / 2.),
            )?;
    
            Ok(())
        })
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
