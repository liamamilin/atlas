import { Component, type ReactNode } from "react";

export class PageBoundary extends Component<{ children: ReactNode; zh: boolean }, { failed: boolean }> {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() {
    if (!this.state.failed) return this.props.children;
    const { zh } = this.props;
    return <main role="alert" className="mx-auto my-16 max-w-xl rounded-2xl border border-border bg-surface p-8 text-center">
      <p className="text-xs font-medium tracking-widest text-danger">APPLICATION ATLAS</p>
      <h1 className="mt-3 font-serif text-2xl">{zh ? "页面加载失败" : "Page failed to load"}</h1>
      <p className="mt-3 text-sm leading-6 text-muted">{zh ? "请重新加载，或通过导航打开其他页面。" : "Reload this page or use the navigation to open another page."}</p>
      <button className="mt-5 rounded-lg bg-primary px-4 py-3 text-sm text-primary-fg" onClick={() => window.location.reload()}>{zh ? "重新加载页面" : "Reload page"}</button>
    </main>;
  }
}
