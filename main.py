# lambda_function.py
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


# Set the OTLP exporter configuration
otlp_exporter = OTLPSpanExporter(
    endpoint="url",
)

# Configure the BatchSpanProcessor
span_processor = BatchSpanProcessor(otlp_exporter)

# Set up the TracerProvider with the exporter and processor
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(span_processor)

# Get the tracer
tracer = trace.get_tracer(__name__)

def main():
    # Extract the Step Function execution ID from the event
    


    # Start a new span for this Lambda function
    with tracer.start_as_current_span("test") as span:
        # Set the correlation ID as an attribute of the span
        span.set_attribute("flow", "1")
        span.set_attribute("sfs", "22")

        # Set environment attribute
        span.set_attribute("environment", "test")

        print("Lambda1 execution")

    # Ensure that spans are exported before the Lambda function exits
    trace.get_tracer_provider().shutdown()

    # Return a response
    return {
        'statusCode': 200,
        'body': 'Lambda1 executed successfully',
    }

main()
