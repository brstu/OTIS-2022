
export class AnyTools {

  convertClass(reg) {
    if (/^"/.test(reg)) {
      if (/:$/.test(reg))
        return 'class="key"'
      else
        return 'class="string"'
    } else {
      if (/true|false/.test(reg)) return 'class="boolean"';
      if (/null/.test(reg)) return 'class="null"';
      return 'class="number"';
    }
  };

  fixOptions(options) {
    options.indent = options.indent || 2;
    options.useTabs = true === options.useTabs;
    return options;
  };

  fixJSON(json) {
    return (typeof json === "string") ? JSON.parse(json) : json;
  };

  highlight(json, options) {
    json = this.fixJSON(json);
    options = this.fixOptions(options);

    var tabs = options.useTabs;
    var indent = options.indent;

    json = JSON.stringify(json, null, (tabs === true ? "\t" : indent));
    json = json.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|\b,\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, (reg) => {

      let out = "<span " + this.convertClass(reg) + ">" + reg + "</span>";
      if (/,/.test(reg))
        out += '<br>';
      return out;
    });
  }
}
