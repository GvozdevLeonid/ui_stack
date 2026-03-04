{%- if cookiecutter.include_alpinejs == "yes" -%}
import Alpine from "alpinejs";


{%- if cookiecutter.include_alpinejs_plugins == "yes" -%}
{% set allowed_plugins = ["mask","intersect","resize","persist","focus","collapse","anchor","morph","sort"] %}
{% set plugins = cookiecutter.alpinejs_plugins | replace(" ", "") %}
{% for plugin in plugins.split(",") if plugin and plugin in allowed_plugins %}
import plugin_{{ loop.index }} from "@alpinejs/{{ plugin }}";
Alpine.plugin(plugin_{{ loop.index }});
{% endfor %}
{% endif %}
window.Alpine = Alpine;
Alpine.start();
{%- endif %}

/* Your custom scripts are below. */