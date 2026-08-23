"""OpenTelemetry bootstrap for Shopping Assistant."""

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def configure_tracing() -> None:
    """Configure OTLP tracing before the Flask app is imported."""
    provider = TracerProvider(
        resource=Resource.create({SERVICE_NAME: "shoppingassistantservice"})
    )
    provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    FlaskInstrumentor().instrument()


configure_tracing()
