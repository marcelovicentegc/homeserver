use tauri::{menu::{MenuBuilder, MenuItem, SubmenuBuilder}, LogicalPosition, LogicalSize, WebviewUrl};

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            let handle = app.handle();
            let quit = MenuItem::new(handle, "Quit", true, None::<&str>)?;
          
            let submenu = SubmenuBuilder::new(app, "Options")
                .items(&[&quit])
                .separator()
                .build()?;

            let open_all = MenuItem::new(handle, "All", true, None::<&str>)?;
            let _open_grafana = &MenuItem::new(handle, "Grafana", true, None::<&str>)?;
            let _open_prometheus = &MenuItem::new(handle, "Prometheus", true, None::<&str>)?;
            let _open_portainer = &MenuItem::new(handle, "Portainer", true, None::<&str>)?;

            let menu = MenuBuilder::new(app).items(&[
                &open_all,
                _open_grafana,
                _open_prometheus,
                _open_portainer,
            ])
                .item(&submenu)
                .build()?;
            let width = 1600.;
            let height = 1200.;
            let window = tauri::window::WindowBuilder::new(app, "sys-o11y")
            .menu(menu)
            .on_menu_event(move |_window, event| {
                if event.id == quit.id() {
                    std::process::exit(0);
                }

                if event.id == open_all.id() {
                    std::println!("TODO: Add state management");
                }
            })
            .inner_size(width, height)
            .title("Sys o11y")
            .build()?;
    
            let _grafana = window.add_child(
            tauri::webview::WebviewBuilder::new(
                "grafana",
                WebviewUrl::External("http://localhost:32911".parse().unwrap()),
            )
            .auto_resize(),
            LogicalPosition::new(width / 2., height / 1.),
            LogicalSize::new(width / 2., height),
            )?;
            let _prometheus = window.add_child(
            tauri::webview::WebviewBuilder::new(
                "prometheus",
                WebviewUrl::External("http://localhost:52441".parse().unwrap()),
            )
            .auto_resize(),
            LogicalPosition::new(width / 2., height / 2.),
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
