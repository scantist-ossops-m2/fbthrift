// @generated by Thrift for thrift/compiler/test/fixtures/doctext/src/module.thrift
// This file is probably not the place you want to edit!

//! Server definitions for `module`.

#![recursion_limit = "100000000"]
#![allow(non_camel_case_types, non_snake_case, non_upper_case_globals, unused_crate_dependencies, unused_imports, clippy::all)]


#[doc(inline)]
pub use :: as types;

pub mod errors {
    #[doc(inline)]
    pub use ::::services::c;
    #[doc(inline)]
    #[allow(ambiguous_glob_reexports)]
    pub use ::::services::c::*;
}

pub(crate) use crate as server;
pub(crate) use ::::services;


#[doc = "Detailed overview of service"]
#[::async_trait::async_trait]
pub trait C: ::std::marker::Send + ::std::marker::Sync + 'static {
    #[doc = "Function doctext."]
    async fn f(
        &self,
    ) -> ::std::result::Result<(), crate::services::c::FExn> {
        ::std::result::Result::Err(crate::services::c::FExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "C",
                "f",
            ),
        ))
    }
    #[doc = "Streaming function"]
    async fn numbers(
        &self,
    ) -> ::std::result::Result<    ::futures::stream::BoxStream<'static, ::std::result::Result<crate::types::number, crate::services::c::NumbersStreamExn>>
, crate::services::c::NumbersExn> {
        ::std::result::Result::Err(crate::services::c::NumbersExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "C",
                "numbers",
            ),
        ))
    }
    #[doc = ""]
    async fn thing(
        &self,
        _a: ::std::primitive::i32,
        _b: ::std::string::String,
        _c: ::std::collections::BTreeSet<::std::primitive::i32>,
    ) -> ::std::result::Result<::std::string::String, crate::services::c::ThingExn> {
        ::std::result::Result::Err(crate::services::c::ThingExn::ApplicationException(
            ::fbthrift::ApplicationException::unimplemented_method(
                "C",
                "thing",
            ),
        ))
    }
}

#[::async_trait::async_trait]
impl<T> C for ::std::boxed::Box<T>
where
    T: C + Send + Sync + ?Sized,
{
    async fn f(
        &self,
    ) -> ::std::result::Result<(), crate::services::c::FExn> {
        (**self).f(
        ).await
    }
    async fn numbers(
        &self,
    ) -> ::std::result::Result<    ::futures::stream::BoxStream<'static, ::std::result::Result<crate::types::number, crate::services::c::NumbersStreamExn>>
, crate::services::c::NumbersExn> {
        (**self).numbers(
        ).await
    }
    async fn thing(
        &self,
        a: ::std::primitive::i32,
        b: ::std::string::String,
        c: ::std::collections::BTreeSet<::std::primitive::i32>,
    ) -> ::std::result::Result<::std::string::String, crate::services::c::ThingExn> {
        (**self).thing(
            a,
            b,
            c,
        ).await
    }
}

#[::async_trait::async_trait]
impl<T> C for ::std::sync::Arc<T>
where
    T: C + Send + Sync + ?Sized,
{
    async fn f(
        &self,
    ) -> ::std::result::Result<(), crate::services::c::FExn> {
        (**self).f(
        ).await
    }
    async fn numbers(
        &self,
    ) -> ::std::result::Result<    ::futures::stream::BoxStream<'static, ::std::result::Result<crate::types::number, crate::services::c::NumbersStreamExn>>
, crate::services::c::NumbersExn> {
        (**self).numbers(
        ).await
    }
    async fn thing(
        &self,
        a: ::std::primitive::i32,
        b: ::std::string::String,
        c: ::std::collections::BTreeSet<::std::primitive::i32>,
    ) -> ::std::result::Result<::std::string::String, crate::services::c::ThingExn> {
        (**self).thing(
            a,
            b,
            c,
        ).await
    }
}


/// Processor for C's methods.
#[derive(Clone, Debug)]
pub struct CProcessor<P, H, R, RS> {
    service: H,
    supa: ::fbthrift::NullServiceProcessor<P, R, RS>,
    _phantom: ::std::marker::PhantomData<(P, H, R, RS)>,
}

struct Args_C_f {
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_C_f {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "C.f"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
        ];
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
        })
    }
}

struct Args_C_numbers {
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_C_numbers {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "C.numbers"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
        ];
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
        })
    }
}

struct Args_C_thing {
    a: ::std::primitive::i32,
    b: ::std::string::String,
    c: ::std::collections::BTreeSet<::std::primitive::i32>,
}

impl<P: ::fbthrift::ProtocolReader> ::fbthrift::Deserialize<P> for self::Args_C_thing {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "deserialize_args", fields(method = "C.thing"))]
    fn read(p: &mut P) -> ::anyhow::Result<Self> {
        static ARGS: &[::fbthrift::Field] = &[
            ::fbthrift::Field::new("a", ::fbthrift::TType::I32, 1),
            ::fbthrift::Field::new("b", ::fbthrift::TType::String, 2),
            ::fbthrift::Field::new("c", ::fbthrift::TType::Set, 3),
        ];
        let mut field_a = ::std::option::Option::None;
        let mut field_b = ::std::option::Option::None;
        let mut field_c = ::std::option::Option::None;
        let _ = p.read_struct_begin(|_| ())?;
        loop {
            let (_, fty, fid) = p.read_field_begin(|_| (), ARGS)?;
            match (fty, fid as ::std::primitive::i32) {
                (::fbthrift::TType::Stop, _) => break,
                (::fbthrift::TType::I32, 1) => field_a = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (::fbthrift::TType::String, 2) => field_b = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (::fbthrift::TType::Set, 3) => field_c = ::std::option::Option::Some(::fbthrift::Deserialize::read(p)?),
                (fty, _) => p.skip(fty)?,
            }
            p.read_field_end()?;
        }
        p.read_struct_end()?;
        ::std::result::Result::Ok(Self {
            a: field_a.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "C.thing", "a"))?,
            b: field_b.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "C.thing", "b"))?,
            c: field_c.ok_or_else(|| ::anyhow::anyhow!("`{}` missing arg `{}`", "C.thing", "c"))?,
        })
    }
}


impl<P, H, R, RS> CProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Frame: ::std::marker::Send + 'static,
    P::Deserializer: ::std::marker::Send,
    H: C,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    pub fn new(service: H) -> Self {
        Self {
            service,
            supa: ::fbthrift::NullServiceProcessor::new(),
            _phantom: ::std::marker::PhantomData,
        }
    }

    pub fn into_inner(self) -> H {
        self.service
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "C.f"))]
    async fn handle_f<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"C";
        const METHOD_NAME: &::std::ffi::CStr = c"f";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"C.f";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_C_f = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.f(
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "C.f", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::info!(method = "C.f", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("C.f", exn);
                ::tracing::error!(method = "C.f", panic = ?aexn);
                ::std::result::Result::Err(crate::services::c::FExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::c::FExn>(
            "f",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "C.numbers"))]
    async fn handle_numbers<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"C";
        const METHOD_NAME: &::std::ffi::CStr = c"numbers";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"C.numbers";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_C_numbers = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.numbers(
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "C.numbers", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("C.numbers", exn);
                ::tracing::error!(method = "C.numbers", panic = ?aexn);
                ::std::result::Result::Err(crate::services::c::NumbersExn::ApplicationException(aexn))
            }
        };

        use ::futures::StreamExt as _;

        let (response, stream) = match res {
            ::std::result::Result::Ok(res) => {
                let response = ::std::result::Result::Ok(());
                let stream = res;

                let stream = ::std::panic::AssertUnwindSafe(stream)
                    .catch_unwind()
                    .map(|item| {
                        match item {
                            ::std::result::Result::Ok(::std::result::Result::Ok(success)) => {
                                let payload = ::fbthrift::help::serialize_stream_item::<P, crate::services::c::NumbersStreamExn>(
                                    ::std::result::Result::Ok(success),
                                    "numbers",
                                );
                                ::fbthrift::SerializedStreamElement::Success(payload)
                            }
                            ::std::result::Result::Ok(::std::result::Result::Err(crate::services::c::NumbersStreamExn::ApplicationException(aexn))) => {
                                tracing::info!(?aexn, method="C.numbers", "Streaming ApplicationException");
                                ::fbthrift::SerializedStreamElement::ApplicationException(aexn)
                            }
                            ::std::result::Result::Err(exn) => {
                                tracing::error!(?exn, method="C.numbers", "Streaming unwind");
                                let aexn = ::fbthrift::ApplicationException::handler_panic("C.numbers", exn);
                                ::fbthrift::SerializedStreamElement::ApplicationException(aexn)
                            }
                        }
                    })
                    .boxed();
                (response, Some(stream))
            },
            ::std::result::Result::Err(exn) => (::std::result::Result::Err(exn), None),
        };

        let response = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::c::NumbersExn>(
            "numbers",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            response,
        )?;

        let _ = reply_state.send_stream_reply(response, stream, P::PROTOCOL_ID);
        Ok(())
    }

    #[::tracing::instrument(skip_all, name = "handler", fields(method = "C.thing"))]
    async fn handle_thing<'a>(
        &'a self,
        p: &'a mut P::Deserializer,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"C";
        const METHOD_NAME: &::std::ffi::CStr = c"thing";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"C.thing";
        let mut ctx_stack = req_ctxt.get_context_stack(SERVICE_NAME, SERVICE_METHOD_NAME)?;
        ::fbthrift::ContextStack::pre_read(&mut ctx_stack)?;
        let _args: self::Args_C_thing = ::fbthrift::Deserialize::read(p)?;
        let bytes_read = ::fbthrift::help::buf_len(&req)?;
        ::fbthrift::ContextStack::on_read_data(&mut ctx_stack, ::fbthrift::SerializedMessage {
            protocol: P::PROTOCOL_ID,
            method_name: METHOD_NAME,
            buffer: req,
        })?;
        ::fbthrift::ContextStack::post_read(&mut ctx_stack, bytes_read)?;

        let res = ::std::panic::AssertUnwindSafe(
            self.service.thing(
                _args.a,
                _args.b,
                _args.c,
            )
        )
        .catch_unwind()
        .await;

        // nested results - panic catch on the outside, method on the inside
        let res = match res {
            ::std::result::Result::Ok(::std::result::Result::Ok(res)) => {
                ::tracing::trace!(method = "C.thing", "success");
                ::std::result::Result::Ok(res)
            }
            ::std::result::Result::Ok(::std::result::Result::Err(exn)) => {
                ::tracing::info!(method = "C.thing", exception = ?exn);
                ::std::result::Result::Err(exn)
            }
            ::std::result::Result::Err(exn) => {
                let aexn = ::fbthrift::ApplicationException::handler_panic("C.thing", exn);
                ::tracing::error!(method = "C.thing", panic = ?aexn);
                ::std::result::Result::Err(crate::services::c::ThingExn::ApplicationException(aexn))
            }
        };

        let env = ::fbthrift::help::serialize_result_envelope::<P, R, crate::services::c::ThingExn>(
            "thing",
            METHOD_NAME,
            _seqid,
            req_ctxt,
            &mut ctx_stack,
            res,
        )?;
        reply_state.send_reply(env);
        Ok(())
    }
}

#[::async_trait::async_trait]
impl<P, H, R, RS> ::fbthrift::ServiceProcessor<P> for CProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Deserializer: ::std::marker::Send,
    H: C,
    P::Frame: ::std::marker::Send + 'static,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    type RequestContext = R;
    type ReplyState = RS;

    #[inline]
    fn method_idx(&self, name: &[::std::primitive::u8]) -> ::std::result::Result<::std::primitive::usize, ::fbthrift::ApplicationException> {
        match name {
            b"f" => ::std::result::Result::Ok(0usize),
            b"numbers" => ::std::result::Result::Ok(1usize),
            b"thing" => ::std::result::Result::Ok(2usize),
            _ => ::std::result::Result::Err(::fbthrift::ApplicationException::unknown_method()),
        }
    }

    #[allow(clippy::match_single_binding)]
    async fn handle_method(
        &self,
        idx: ::std::primitive::usize,
        _p: &mut P::Deserializer,
        _req: ::fbthrift::ProtocolDecoded<P>,
        _req_ctxt: &R,
        _reply_state: ::std::sync::Arc<RS>,
        _seqid: ::std::primitive::u32,
    ) -> ::anyhow::Result<()> {
        match idx {
            0usize => {
                self.handle_f(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            1usize => {
                self.handle_numbers(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            2usize => {
                self.handle_thing(_p, _req, _req_ctxt, _reply_state, _seqid).await
            }
            bad => panic!(
                "{}: unexpected method idx {}",
                "CProcessor",
                bad
            ),
        }
    }

    #[allow(clippy::match_single_binding)]
    #[inline]
    fn create_interaction_idx(&self, name: &str) -> ::anyhow::Result<::std::primitive::usize> {
        match name {
            _ => ::anyhow::bail!("Unknown interaction"),
        }
    }

    #[allow(clippy::match_single_binding)]
    fn handle_create_interaction(
        &self,
        idx: ::std::primitive::usize,
    ) -> ::anyhow::Result<
        ::std::sync::Arc<dyn ::fbthrift::ThriftService<P::Frame, Handler = (), RequestContext = Self::RequestContext, ReplyState = Self::ReplyState> + ::std::marker::Send + 'static>
    > {
        match idx {
            bad => panic!(
                "{}: unexpected method idx {}",
                "CProcessor",
                bad
            ),
        }
    }

    async fn handle_on_termination(&self) {
    }
}

#[::async_trait::async_trait]
impl<P, H, R, RS> ::fbthrift::ThriftService<P::Frame> for CProcessor<P, H, R, RS>
where
    P: ::fbthrift::Protocol + ::std::marker::Send + ::std::marker::Sync + 'static,
    P::Deserializer: ::std::marker::Send,
    P::Frame: ::std::marker::Send + 'static,
    H: C,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = <P as ::fbthrift::Protocol>::Frame>
        + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<P::Frame, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::ProtocolDecoded<P>: ::std::clone::Clone,
    ::fbthrift::ProtocolEncodedFinal<P>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    type Handler = H;
    type RequestContext = R;
    type ReplyState = RS;

    #[tracing::instrument(level="trace", skip_all, fields(service = "C"))]
    async fn call(
        &self,
        req: ::fbthrift::ProtocolDecoded<P>,
        req_ctxt: &R,
        reply_state: ::std::sync::Arc<RS>,
    ) -> ::anyhow::Result<()> {
        use ::fbthrift::{ProtocolReader as _, ServiceProcessor as _};
        let mut p = P::deserializer(req.clone());
        let (idx, mty, seqid) = p.read_message_begin(|name| self.method_idx(name))?;
        if mty != ::fbthrift::MessageType::Call {
            return ::std::result::Result::Err(::std::convert::From::from(::fbthrift::ApplicationException::new(
                ::fbthrift::ApplicationExceptionErrorCode::InvalidMessageType,
                format!("message type {:?} not handled", mty)
            )));
        }
        let idx = match idx {
            ::std::result::Result::Ok(idx) => idx,
            ::std::result::Result::Err(_) => {
                return self.supa.call(req, req_ctxt, reply_state).await;
            }
        };
        self.handle_method(idx, &mut p, req, req_ctxt, reply_state, seqid).await?;
        p.read_message_end()?;

        Ok(())
    }

    fn create_interaction(
        &self,
        name: &str,
    ) -> ::anyhow::Result<
        ::std::sync::Arc<dyn ::fbthrift::ThriftService<P::Frame, Handler = (), RequestContext = R, ReplyState = RS> + ::std::marker::Send + 'static>
    > {
        use ::fbthrift::{ServiceProcessor as _};
        let idx = self.create_interaction_idx(name);
        let idx = match idx {
            ::anyhow::Result::Ok(idx) => idx,
            ::anyhow::Result::Err(_) => {
                return self.supa.create_interaction(name);
            }
        };
        self.handle_create_interaction(idx)
    }

    fn get_method_names(&self) -> &'static [&'static str] {
        &[
            // From module.C:
            "f",
            "numbers",
            "thing",
        ]
    }

    async fn on_termination(&self) {
        use ::fbthrift::{ServiceProcessor as _};
        self.handle_on_termination().await
    }
}

/// Construct a new instance of a C service.
///
/// This is called when a new instance of a Thrift service Processor
/// is needed for a particular Thrift protocol.
#[::tracing::instrument(level="debug", skip_all, fields(proto = ?proto))]
pub fn make_C_server<F, H, R, RS>(
    proto: ::fbthrift::ProtocolID,
    handler: H,
) -> ::std::result::Result<::std::boxed::Box<dyn ::fbthrift::ThriftService<F, Handler = H, RequestContext = R, ReplyState = RS> + ::std::marker::Send + 'static>, ::fbthrift::ApplicationException>
where
    F: ::fbthrift::Framing + ::std::marker::Send + ::std::marker::Sync + 'static,
    H: C,
    R: ::fbthrift::RequestContext<Name = ::std::ffi::CStr> + ::std::marker::Send + ::std::marker::Sync + 'static,
    <R as ::fbthrift::RequestContext>::ContextStack: ::fbthrift::ContextStack<Name = R::Name, Frame = F> + ::std::marker::Send + ::std::marker::Sync + 'static,
    RS: ::fbthrift::ReplyState<F, RequestContext = R> + ::std::marker::Send + ::std::marker::Sync + 'static,
    ::fbthrift::FramingDecoded<F>: ::std::clone::Clone,
    ::fbthrift::FramingEncodedFinal<F>: ::std::clone::Clone + ::fbthrift::BufExt,
{
    match proto {
        ::fbthrift::ProtocolID::BinaryProtocol => {
            ::std::result::Result::Ok(::std::boxed::Box::new(CProcessor::<::fbthrift::BinaryProtocol<F>, H, R, RS>::new(handler)))
        }
        ::fbthrift::ProtocolID::CompactProtocol => {
            ::std::result::Result::Ok(::std::boxed::Box::new(CProcessor::<::fbthrift::CompactProtocol<F>, H, R, RS>::new(handler)))
        }
        bad => {
            ::tracing::error!(method = "C.", invalid_protocol = ?bad);
            ::std::result::Result::Err(::fbthrift::ApplicationException::invalid_protocol(bad))
        }
    }
}
